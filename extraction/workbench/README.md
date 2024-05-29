# Connectome Workbench metadata extraction

```bash
cd source/workbench
cmake
cd build

# Build only the wb_command executable, this skips building the GUI
make -j16 wb_command

# Copy the dump script and the list of commands to the build directory
cp ../../dump.sh .
cp ../../out_commands.txt .

# Run the dump script
./dump.sh

cd ../..

# Generate the Boutiques descriptors
python generate_descriptors.py
```
