import os


def add_files(file_path, files_dict):
    clean_file = file_path.split("/")[-1]
    file_name, file_ext = clean_file.split(".")

    if file_ext not in files_dict.keys():
        files_dict[file_ext] = []
    files_dict[file_ext].append(file_name)

all_files = {}
directory_name = input()
report_file_path = os.path.join(directory_name, "report.txt")

# check if the report.txt file already exists from previous creation
# if it exists - delete it
if os.path.exists(report_file_path):
    os.remove(report_file_path)

for file in os.listdir(directory_name):
    f = os.path.join(directory_name, file)

    # if it's a folder
    if os.path.isdir(f):
        for el in os.listdir(f):
            inner_f = os.path.join(f, el)

            # only proceed if it's not a folder
            if not os.path.isdir(inner_f):
                add_files(inner_f, all_files)

    else:
        add_files(f, all_files)

sorted_files = dict(sorted(all_files.items(), key=lambda x: (x[0], x[1])))

output_lines = []
for ext, names in sorted_files.items():
    output_lines.append(f".{ext}")
    for name in names:
        output_lines.append(f"- - - {name}.{ext}")

with open(report_file_path, "w") as report:
    report.write("\n".join(output_lines))
