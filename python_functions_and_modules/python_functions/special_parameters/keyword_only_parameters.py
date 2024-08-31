
# Keyword-only parameters are parameters that must be specified by keyword. 

def configure_profile(*, language, region):    # The `*` symbol ensures all parameters after it are specified by keyword only. 
    return f"Language: {language}, Region: {region}"

print(configure_profile(language="Kiswahili", region="Kenya")) # Output: Language: Kiswahili, Region: Kenya.
      
      