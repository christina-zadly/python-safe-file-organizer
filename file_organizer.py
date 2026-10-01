from pathlib import Path
def scan_folder(folder_path):
    """
    Scans the given folder path and returns a list of files in it.
    Returns:
         list[Path]: A list of Path objects representing the files in the folder.
        None: If the path does not exist or is not a directory.
    """
    if folder_path.exists() and folder_path.is_dir():
        return[item for item in folder_path.iterdir()if item.is_file() ]
    
    else:
       return None 
def prepare_preview_data(files):
    """
    Categorizes the given file paths by their file extensions
    and returns them as a dictionary.

    Returns:
        dict: A dictionary containing file categories and
        the file paths belonging to each category.
    """
    extension_map = {
        ".pdf": "Documents", ".txt": "Documents", ".doc": "Documents", ".docx": "Documents", ".rtf": "Documents", ".odt": "Documents",
        ".jpg": "Images", ".jpeg": "Images", ".png": "Images", ".gif": "Images", ".bmp": "Images", ".webp": "Images", ".svg": "Images",
        ".csv": "Spreadsheets", ".xls": "Spreadsheets", ".xlsx": "Spreadsheets", ".ods": "Spreadsheets",
        ".ppt": "Presentations", ".pptx": "Presentations", ".odp": "Presentations",
        ".mp4": "Videos", ".avi": "Videos", ".mkv": "Videos", ".mov": "Videos", ".wmv": "Videos", ".webm": "Videos",
        ".mp3": "Audio", ".wav": "Audio", ".flac": "Audio", ".aac": "Audio", ".ogg": "Audio", ".m4a": "Audio",
        ".zip": "Archives", ".rar": "Archives", ".7z": "Archives", ".tar": "Archives", ".gz": "Archives",
        ".exe": "Applications",
        ".py": "Code", ".js": "Code", ".html": "Code", ".css": "Code", ".java": "Code", ".c": "Code", ".cpp": "Code", ".sql": "Code",
        ".json": "Data", ".xml": "Data", ".yaml": "Data", ".yml": "Data", ".db": "Data", ".sqlite": "Data"
    }

    categorized_files={
        "Documents"  :[],
        "Images" : [],
        "Spreadsheets"  :[],
        "Presentations" : [],
        "Videos" : [],
        "Audio": [],
        "Archives": [],
        "Applications": [],
        "Code" : [],
        "Data" : [],
        "Other" : []
    }
    for item in files:
        ext = item.suffix.lower() 
        category = extension_map.get(ext, "Other")
        categorized_files[category].append(item)
    return categorized_files
def preview_before_modification(files,categorized_files):
    """
        Displays a preview of the file organization and asks the user
        for confirmation before making any changes.
    
        Returns:
            tuple: The user's decision and a dictionary containing
            non-empty categories with their corresponding file paths.
    """
    non_empty_categories={}
    print("Preview")
    print("-"*30)
    print(f"{'Total files':<10}: {len(files)}")
    print("-"*30)
    for key,value in categorized_files.items():
        if len(value)>0:
            print(f"{key:<10}:  {len(value)}")
            non_empty_categories[key]=value
    print("-"*30)
   
    while True:
        user_decision=input("Do you wish to proceed? (Yes/No): ").strip().lower()
        if user_decision == "yes":
            return user_decision, non_empty_categories
        elif  user_decision == "no":
             return user_decision,{}
        
def organize_files(base_path,categorized_files):
    """
    Creates the main organization folder and subfolders for each file category,
    then moves the files into their corresponding folders.

    Returns:
        dict: A dictionary containing the number of successfully moved files
        and information about skipped or failed files, if any.
    """
    main_folder=base_path /"Organized_Files"
    main_folder.mkdir(exist_ok=True)
    operation_result={"Successful": 0,"Skipped": [],"Failed": []}
    for key, value in categorized_files.items():
        sub_folder= main_folder / key
        sub_folder.mkdir(exist_ok=True)
        
        for item in value:
            destination= sub_folder / item.name
            counter=1
            while destination.exists():
                new_name=f"{item.stem}({counter}){item.suffix}"
                destination= sub_folder / new_name
                counter+=1

            try:
                item.rename(destination)
                operation_result["Successful"]+=1
            except PermissionError:
                # If the file is protected or open in another program
                operation_result["Skipped"].append((item.name,"️Access Denied"))
            except Exception as e:
                # For any other unexpected error
                operation_result["Failed"].append((item.name,str(e)))
                
    
    return operation_result

def generate_report(results,files):
    """
      Generates and displays the final report of the file organization process, including the total number of files,
      successfully moved files, skipped files, and failed files with their details.

      Returns:
        None: This function displays the report and does not return a value.
        """
    print("="*50)
    print("File Organization Report".center(50))
    print("="*50, end="\n")
    print(f"Total Files:{len(files):>15}")
    print(f"Successful: {results['Successful']:>15}")
    print(f"Skipped:    {len(results['Skipped']):>15}")
    print(f"Failed:     {len(results['Failed']):>15}")
    
    print("-"*50)
    for key, value in results.items():
        if key=="Skipped" and len(value)>0:
            print(f"{key} Files:")
            for item in value:
                print(f'-{item[0]} =>  {item[1]}')
            
        elif key=="Failed" and len(value)>0:
            print(f"{key} Files:")
            for item in value:
                print(f'-{item[0]} =>  {item[1]}')
            
    print("="*50)







def main():
    """ 
    Controls the main workflow of the file organizer. 
    It gets the folder path from the user and runs the file organization process.
    """
    while True:
        user_input=input('Enter File Path: ').strip()
        files=scan_folder(Path(user_input))   
        if files is None:
            print("The folder was not found. Please enter the correct path.\n")
        else:
            break
        
    categorized_files=prepare_preview_data(files)
    decision,non_empty_categories= preview_before_modification(files,categorized_files)
    if decision == "yes":
       result=organize_files(Path(user_input),non_empty_categories)
       generate_report(result,files)
    else:
        print("Operation cancelled. No changes were made to your files.")
        print("Thank you for using the File Organizer.")
if __name__ =="__main__":
    main()