{
    "targets": [
        {
            "target_name": "<(module_name)",
            "type": "none",
            "sources": [ "src/hello.cc" ],
            "conditions": [
                ["OS == 'win'", {
                    "defines": [
                        "WIN32",
                        "UNICODE",
                    ],
                    "libraries": ["shell32.lib"],
                    "configurations" : {
                        "Debug" : {
                            "msvs_settings": {
                                "VCCLCompilerTool": {
                                    "RuntimeLibrary": "3" # /MDd
                                },
                                "VCLinkerTool": {
                                    "AdditionalOptions": ["/ignore:4099"],
                                    "IgnoreDefaultLibraryNames": ["libcmtd.lib"]
                                }
                            }
                        },
                        "Release" : {
                            "msvs_settings": {
                                "VCCLCompilerTool": {
                                    "RuntimeTypeInfo": "true", # To disable "/GR-"
                                    "RuntimeLibrary": "2" # /MDd
                                },
                                "VCLinkerTool": {
                                    "AdditionalOptions": ["/ignore:4099"],
                                    "IgnoreDefaultLibraryNames": ["libcmt.lib"]
                                }
                            }
                        }
                    }
                }],
            ]
        },
        {
            "target_name": "action_after_build",
            "type": "none",
            "dependencies": [ "<(module_name)" ],
            "copies": [
                {
                    "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
                    "destination": "<(module_path)"
                }
            ]
        }
    ]
}
