## Yourkit MCP Converter

The Yourkit MCP converter can apply a MCP mappings file (methods.csv) to a Yourkit snapshot file. This way, the trace 
backs become much more legible. To run it, download the appropriate MCP mappings from [here](http://export.mcpbot.bspk.rs/) 
by using the download ZIP option, extract the methods.csv and then run the tool with the appropriate arguments (there's 
a --help available for more info).

### Disclaimer

This software is in no way associated with the Yourkit product or the YourKit GmbH. The code was written using a hex 
editor on the snapshot file and searching for the `func_*` strings. It is assumed that the byte prefixing this is the 
length of the function name, but that might be an invalid assumption.  