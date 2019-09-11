import os,re,csv
import tempfile
from pdf2image import convert_from_path
from constants import *

def get_text(image,pattern):
	var = os.popen('./ReadBarcode {file}'.format(file=image)).read()
	try:
		values = re.search(pattern,var).group(0)
		return values
	except Exception as e:
		print(str(e))

def clear_data(values):
	values[0] = values[0].replace("Value:","")
	values[-1] = values[-1].replace("\r","").replace("\n","")
	vals = [x.strip() for x in values]

	return vals

def initialize_csv(output_file):
    os.remove(output_file) if os.path.exists(output_file) else None
    file_obj = csv.writer(open(output_file,'w'))
    return file_obj

def extract_as_image(filename,save_dir):
	with tempfile.TemporaryDirectory() as path:
		images_from_path = convert_from_path(filename, output_folder=path, last_page=2, first_page =0)

	base_filename  =  os.path.splitext(os.path.basename(filename))[0]
	create_dir(save_dir)

	i = 1
	for page in images_from_path:
		image_name = base_filename+str(i)+".jpg"
		page.save(os.path.join(save_dir, image_name), 'JPEG')
		i += 1


def create_dir(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)


def list_files(directory, extension):
        for (dirpath, dirnames, filenames) in os.walk(directory):
            return (os.path.join(dirpath,f) for f in filenames if f.endswith('.' + extension))

if __name__=="__main__":
	extract_as_image(filename,save_dir)
	all_files = list_files(save_dir,"jpg")
	file = initialize_csv(output_file)
	file.writerow(headers)
	for image in all_files:
		values = get_text(image,pattern)
		if values:
			values = values.split('\t')
			values = clear_data(values)
			file.writerow(values)
			




	