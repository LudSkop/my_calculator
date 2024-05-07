# Робота з архівами.
import shutil
   

print(shutil.get_archive_formats())
archive = shutil.make_archive('archive_file_name', 'zip','Hello')
print(archive)

shutil.unpack_archive(archive, 'Archive')









