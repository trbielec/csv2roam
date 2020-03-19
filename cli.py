from csv import DictReader
import click


@click.command()
@click.option('--root-page', '-r', is_flag=True, help='Create [[page]] for root values (first column)')
@click.option('--child-pages', '-c', is_flag=True, help='Create [[page]] for child values')
@click.argument('input', type=click.Path(exists=True))
@click.argument('output', type=click.Path(exists=True))
def main(input, output, root_page, child_pages):
    """Converts CSV file to nested markdown format supported by Roam Research"""

    # open file in read mode
    with open(input, 'r') as read_obj:
        # pass the file object to DictReader() to get the DictReader object
        dict_reader = DictReader(read_obj)
        # get a list of dictionaries from dct_reader
        list_of_dict = list(dict_reader)
        print(len(list_of_dict), " rows in input file")
        # print list of dict i.e. rows
        # print(list_of_dict)

        # print('**** Print dictionaries into Roam format ****')
        f = open(output, 'w+')
        f.write("# Data Export\n")
        fstring = ''
        for dic in list_of_dict:
            i = 0
            for key in dic:
                # first column values are at the root (no indent)
                if i == 0:
                    if root_page:
                        # create a [[page]] for root values (first column)
                        fstring = "- "+key+":: [["+dic[key]+"]]\n"
                    else:
                        fstring = "- "+key+":: "+dic[key]+"\n"
                    f.write(fstring)
                    i = i+1
                else:
                    # skip empty values
                    if dic[key] != '':
                        # indent remaining values
                        if child_pages:
                            # create a [[page]] for all child values
                            fstring = "  - "+key+":: [["+dic[key]+"]]\n"
                        else:
                            fstring = "  - "+key+":: "+dic[key]+"\n"
                        f.write(fstring)
                        i = i+1
        f.close()
        print("Output successful: ", output)
