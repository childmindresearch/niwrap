from enum import Enum
from typing import Annotated, Any, Optional, Union

from pydantic import BaseModel, Field, StringConstraints, model_validator


# Definition for inputs
class InputTypeEnum(str, Enum):
    STRING = "String"
    FILE = "File"
    FLAG = "Flag"
    NUMBER = "Number"


class IOModel(BaseModel):
    id: Annotated[str, StringConstraints(pattern=r"^[0-9,_,a-z,A-Z]*$")] = Field(
        description='A short, unique, informative identifier containing only alphanumeric characters and underscores. Typically used to generate variable names. Example: "data_file".',
        min_length=1,
    )
    name: str = Field(
        description="A human-readable name. Example: 'Data file'.",
        min_length=1,
    )
    description: Optional[str] = Field(default=None)
    value_key: str = Field(
        alias="value-key",
        description="A string contained in command-line, substituted by the input value and/or flag at runtime.",
    )
    list_: bool = Field(
        alias="list",
        description='True if list of values. If value is of type "Flag" cannot be a list.',
        default=False,
    )
    optional: bool = Field(description="True if optional", default=False)
    command_line_flag: Optional[str] = Field(
        alias="command-line-flag",
        description='Option flag, involved in the value-key substitution. Inputs of type "Flag" have to have a command-line flag. Examples: -v, --force.',
        default=None,
    )
    command_line_flag_separator: Optional[str] = Field(
        alias="command-line-flag-separator",
        description="Separator used between flags and their arguments. Defaults to a single space.",
        default=None,
    )
    uses_absolute_path: bool = Field(
        alias="uses-absolute-path",
        description="Specifies value must be given as an absolute path.",
        default=False,
    )

    @model_validator(mode="before")
    def validate_dependencies(cls, values):
        if (
            values
            and values.get("command_line_flag_separator")
            and not values.get("command_line_flag")
        ):
            raise ValueError(
                "Field 'command_line_flag_separator' requires 'command_line_flag' to be set."
            )
        return values

    class Config:
        populate_by_name = True
        use_enum_values = True


class SubCommandInput(BaseModel):
    id: Annotated[str, StringConstraints(pattern=r"^[0-9,_,a-z,A-Z]+$")]
    name: str
    description: Optional[str] = Field(default=None)
    command_line: Optional[str] = Field(alias="command-line", default=None)
    inputs: Optional[list["BoutiquesInput"]] = Field(
        description="An array of input objects.", default=None
    )
    output_files: Optional[list[str]] = Field(alias="output-files", default=None)
    groups: Optional[list[str]] = Field(default=None)


class BoutiquesInput(IOModel):
    type_: Union[
        InputTypeEnum,
        SubCommandInput,
        list[SubCommandInput],
    ] = Field(alias="type")
    list_separator: Optional[str] = Field(
        alias="list-seperator",
        description="Separator used between list items. Defaults to a single space.",
        default=None,
    )
    requires_inputs: Optional[list[str]] = Field(
        alias="requires-inputs",
        description="Ids of the inputs or ids of groups whose members must be active for this input to be available.",
        default=None,
    )
    disables_inputs: Optional[list[str]] = Field(
        alias="disables-inputs",
        description="Ids of the inputs that are disabled when this input is active.",
        default=None,
    )
    default_value: Optional[Any] = Field(
        alias="default-value",
        description="Default value of the input. The default value is set when no value is specified, even when the input is optional. If the desired behavior is to omit the input from the command line when no value is specified, then no default value should be used. In this case, the tool might still use a default value internally, but this will remain undocumented in the Boutiques interface.",
        default=None,
    )
    value_choices: Optional[list[float | str]] = Field(
        alias="value-choices",
        description="Permitted choices for input value. May not be used with the Flag type.",
        default=None,
    )
    value_requires: Optional[Any] = Field(  # Field not used
        alias="value-requires",
        description="Ids of the inputs that are required when the corresponding value choice is selected.",
        deprecated=True,
    )
    value_disables: Optional[Any] = Field(  # Field not used
        alias="value-disables",
        description="Ids of the inputs that are disabled when the corresponding value choice is selected.",
        deprecated=True,
    )
    integer: bool = Field(
        description="Specify whether the input should be an integer. May only be used with Number type inputs.",
        default=False,
    )
    minimum: Optional[float] = Field(
        description="Specify the minimum value of the input (inclusive). May only be used with Number type inputs.",
        default=None,
    )
    maximum: Optional[float] = Field(
        description="Specify the maximum value of the input (inclusive). May only be used with Number type inputs.",
        default=None,
    )
    exclusive_minimum: bool = Field(
        alias="exclusive-minimum",
        description="Specify whether the minimum is exclusive or not. May only be used with Number type inputs.",
        default=False,
    )
    exclusive_maximum: bool = Field(
        alias="exclusive-maximum",
        description="Specify whether the maximum is exclusive or not. May only be used with Number type inputs.",
        default=False,
    )
    min_list_entries: Optional[float] = Field(
        alias="min-list-entries",
        description="Specify the minimum number of entries in the list. May only be used with List type inputs.",
        default=None,
    )
    max_list_entries: Optional[float] = Field(
        alias="max-list-entries",
        description="Specify the maximum number of entries in the list. May only be used with List type inputs.",
        default=None,
    )
    resolve_parent: bool = Field(
        alias="resolve-parent",
        description="Specifies that the full parent directory of this file needs to be visible to the tool. Only specifiable for File type inputs.",
        default=False,
    )
    mutable: bool = Field(
        description="Specifies that the tool may modify the input file. Only specifiable for File type inputs.",
        default=False,
    )

    @model_validator(mode="before")
    def validate_type(cls, values):
        if values.get("type") == "Flag" and values.get("list"):
            raise ValueError("If type is 'Flag', 'list' must be false.")
        return values

    @model_validator(mode="before")
    def validate_dependencies(cls, values):
        """Validate parameter dependencies."""

        def _raise_field_error(field: str, condition: str):
            """Helper to raise field-related errors."""
            raise ValueError(f"Field '{field}' {condition}")

        type_value = values.get("type")

        # Dependency validation
        if (
            values.get("min_list_entries") is not None
            or values.get("max_list_entries") is not None
        ) and not values.get("list"):
            _raise_field_error(
                "min_list_entries and max_list_entries",
                "can only be set if 'list' is true.",
            )

        if values.get("list_separator") and not values.get("list"):
            _raise_field_error("list_separator", "can only be set if 'list' is true.")

        number_related_fields = ["integer", "minimum", "maximum"]
        for field in number_related_fields:
            if values.get(field) and type_value != "Number":
                _raise_field_error(field, "can only be set if 'type' is 'Number'.")

        if values.get("uses_absolute_path") and type_value != "File":
            _raise_field_error(
                "uses_absolute_path", "can only be set if 'type' is 'File'."
            )

        if values.get("exclusive_minimum") and values.get("minimum") is None:
            _raise_field_error(
                "exclusive_minimum", "can only be set if 'minimum' is provided."
            )
        if values.get("exclusive_maximum") and values.get("maximum") is None:
            _raise_field_error(
                "exclusive_maximum", "can only be set if 'maximum' is provided."
            )

        for field in ["value_disables", "value_enables"]:
            if values.get(field) and values.get("value_choices") is None:
                _raise_field_error(
                    field, "can only be set if 'value_choices' are provided."
                )

        return values


# Rebuild to allow for forward references for nested inputs
BoutiquesInput.model_rebuild()


class PathProperty(BaseModel):
    propertyNames: Annotated[
        str, StringConstraints(pattern=r"^[A-Za-z0-9_><=!)( ]*$")
    ] = Field(default=None)


class OutputFile(IOModel):
    path_template: Optional[str] = Field(
        alias="path-template",
        description='Describes the output file path relatively to the execution directory. May contain input value keys and wildcards. Example: "results/[INPUT1]_brain*.mnc".',
        min_length=1,
        default=None,
    )
    conditional_path_template: Optional[list[PathProperty]] = Field(
        alias="conditional-path-template",
        description='List of objects containing boolean statement (Limited python syntax: ==, !=, <, >, <=, >=, and, or) and output file paths relative to the execution directory, assign path of first true boolean statement. May contain input value keys, "default" object required if "optional" set to True . Example list: "[{"[PARAM1] > 8": "outputs/[INPUT1].txt"}, {"default": "outputs/default.txt"}]".',
        min_length=1,
        default=None,
    )
    path_template_stripped_extensions: Optional[list[str]] = Field(
        alias="path-template-stripped-extensions",
        description='List of file extensions that will be stripped from the input values before being substituted in the path template. Example: [".nii",".nii.gz"].',
        default=None,
    )
    file_template: Optional[list[str]] = Field(
        alias="file-template",
        description="An array of strings that may contain value keys. Each item will be a line in the configuration file.",
        min_length=1,
        default=None,
    )

    @model_validator(mode="before")
    def one_of(cls, values):
        """Check one of the listed properties exist."""
        if values.get("path_template") and values.get("conditional_path_template"):
            raise ValueError(
                "Only one of 'path-template' or 'conditional-path-template' should be provided."
            )

    @model_validator(mode="before")
    def any_of(cls, values):
        """Validate parameter dependencies."""
        # 'anyOf' condition
        file_template = values.get("file_template")
        list_value = values.get("list")
        if not file_template:
            return values
        elif (
            isinstance(file_template, list)
            and len(file_template) >= 1
            and list_value is False
        ):
            return values
        raise ValueError(
            'Either "file-template" should be a non-empty list of strings and "list" should be False, '
            'or "file-template" should be False.'
        )
