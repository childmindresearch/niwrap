#!/bin/bash

function prepend {
  echo -e "$1" | cat - "$2" > "$2".tmp && mv "$2".tmp "$2"
}


# Generating documentation for all commands

mrtrix_root="./"
export PATH=$mrtrix_root/bin:"$PATH"
dirpath=${mrtrix_root}'/json_docs/reference/commands'
export LC_ALL=C


# Erase legacy files
rm -rf ${mrtrix_root}/docs/reference/scripts ${mrtrix_root}/docs/reference/scripts_list.rst


echo "
.. _list-of-mrtrix3-commands:

########################
List of MRtrix3 commands
########################

" > ${mrtrix_root}/json_docs/reference/commands_list.json


rm -rf   ${mrtrix_root}/json_docs/reference/commands
mkdir -p ${mrtrix_root}/json_docs/reference/commands
toctree_file=$(mktemp)
table_file=$(mktemp)

echo "

.. toctree::
    :hidden:
" > $toctree_file

echo "

.. csv-table::
    :header: \"Lang\", \"Command\", \"Synopsis\"
" > $table_file

cmdlist=""
for n in `find "${mrtrix_root}"/cmd/ -name "*.cpp"`; do
  cmdlist=$cmdlist$'\n'`basename $n`
done
#for n in `find "${mrtrix_root}"/bin/ -type f -print0 | xargs -0 grep -l "import mrtrix3"`; do
  #cmdlist=$cmdlist$'\n'`basename $n`
#done

for n in `echo "$cmdlist" | sort`; do
  cmdname=${n%".cpp"}
  cmdpath=$cmdname
  logopath="python.png"
  case $n in *.cpp)
    if [ "$OSTYPE" == "cygwin" ] || [ "$OSTYPE" == "msys" ] || [ "$OSTYPE" == "win32" ]; then
      cmdpath=${cmdpath}'.exe'
    fi
    logopath="cpp.png"
    ;;
  esac
  touch $dirpath/$cmdname.json
  $cmdpath __print_usage_json__ > $dirpath/$cmdname.json
  #case $n in *.cpp)
  #  prepend ".. _${cmdname}:\n\n${cmdname}\n===================\n" $dirpath/$cmdname.json
  #esac
  echo '    commands/'"$cmdname" >> $toctree_file
  echo '    |'"$logopath"'|, :ref:`'"$cmdname"'`, "'`$cmdpath __print_synopsis__`'"' >> $table_file
done
cat $toctree_file $table_file >> ${mrtrix_root}/json_docs/reference/commands_list.rst
rm -f $toctree_file $table_file
echo "

.. |cpp.png| image:: cpp.png
   :alt: C++

.. |python.png| image:: python.png
   :alt: Python
" >> ${mrtrix_root}/json_docs/reference/commands_list.rst






# Generating list of configuration file options

grep -rn --include=\*.h --include=\*.cpp '^\s*//CONF\b' "${mrtrix_root}" |\
  "${mrtrix_root}"/docs/format_config_options > ${mrtrix_root}/json_docs/reference/config_file_options.rst





# Generating list of environment variables

grep -rn --include=\*.h --include=\*.cpp '^\s*//ENVVAR\b' "${mrtrix_root}" |\
  "${mrtrix_root}"/docs/format_environment_variables > ${mrtrix_root}/json_docs/reference/environment_variables.rst

