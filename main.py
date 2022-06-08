import argparse
import os
import os.path as path
import sys
import glob


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('caminho', help='Caminho para o diretório que contem os arquivos')
    parser.add_argument('--extensao', help='Extensão dos arquivos a serem renomeados', default='.txt')
    parser.add_argument('--prefixo', help='Prefixo usado no nome do arquivo', default='doc_')
    args = parser.parse_args()

    if not path.isdir(args.caminho):
        sys.stderr.write(f'Caminho {args.caminho} não aponta para um diretório válido')
        return sys.exit(-1)

    arquivos = glob.glob(path.join(args.caminho, '*' + args.extensao))

    for numero, arquivo in enumerate(arquivos):
        os.rename(arquivo, path.join(args.caminho, args.prefixo + str(numero) + args.extensao))


if __name__ == '__main__':
    main()
