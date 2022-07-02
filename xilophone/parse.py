import argparse
import read_txt_files
from examples import nose

parser = argparse.ArgumentParser(description="Execute the metallophone")
parser.add_argument("-p", "--score",type=str, action="store",
help="File with the notes and the duration of each one")
parser.add_argument("-d", "--ip", action="store", type=str,
help="The ip of the metallophone")

args = parser.parse_args()
score = args.score
ip = args.ip

list_score = read_txt_files.music_sheet_x(score)
read_txt_files.sorting_notes(list_score)

notes = nose.create_xilophone(list_score)
nose.main(notes)




