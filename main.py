import click

from file_utils import find_directories, get_archive_data
from align import align_files

@click.command()
@click.option('--in_dir', '-i', help='Input folder')
@click.option('--out_dir', '-o', help='Output folder')
@click.option('--request_id', '-r', help='LCO Request ID')
@click.option('--no_download', '-n', help='Use data that has already been downloaded', is_flag=True)
@click.option('--planet', '-p', help='Name of planet')
@click.option('--filter_name','-f', help='Filter code')
@click.option('--stamp', '-s', help='Add timestamp', is_flag=True)
def main(in_dir, out_dir, request_id, no_download, planet, filter_name, stamp):
    if out_dir and request_id and no_download:
        file_group = find_directories(out_dir, request_id, filter_name)
    elif request_id and not no_download:
        get_archive_data(out_dir, request_id)
        file_group = find_directories(out_dir, request_id, filter_name)
    align_files(file_group, out_dir, stamp)
    return

if __name__ == '__main__':
    main()
