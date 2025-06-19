# -*- coding: utf-8 -*-
import hashlib
import csv


class Md5Func:
    def __init__(self):
        pass

    @staticmethod
    def to_md5(target):
        m = hashlib.md5()
        m.update(target.encode('utf-8'))
        return m.hexdigest()

    def transfer_func(self, csv_reader, csv_writer):
        for row in csv_reader:
            row_list = list(row)
            # print(row_list)
            if str(row[0]).find('name') > 0:
                row_list.append('id_md5')
                row_list.append('num_md5')
            else:
                row_list.append(self.to_md5(row[1]))
                row_list.append(self.to_md5(row[2]))
            print(row_list)
            csv_writer.writerow(row_list)
        return csv_writer

    def main(self, path_input, data):
        data_out = open((path_input + '/{name}_md5.csv').format(name=data.split('.')[0]), 'w', encoding='utf8',
                        newline='')
        csv_writer = csv.writer(data_out)
        data_in = open((path_input + '/{dataset}').format(dataset=data), encoding='utf-8')
        csv_reader = csv.reader(data_in)
        self.transfer_func(csv_reader, csv_writer)
        data_out.close()
        data_in.close()


if __name__ == '__main__':
    path_in = './'
    Md5Func().main(path_in, 'abc.csv')
