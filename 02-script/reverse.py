def reverse_string(s):
    return s[::-1]

def reverse(debugger, command, result, internal_dict):
    s1 = "FT_"
    s2 = reverse_string(str(debugger.GetSelectedTarget()))
    print (s1+s2)

def __lldb_init_module(debugger, dict):
	debugger.HandleCommand('command script add -f reverse.reverse reverse')

