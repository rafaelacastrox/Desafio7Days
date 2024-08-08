import openpyxl

file_path = 'DADOS TOTAIS.xlsx'

try:
    # Carregar o workbook
    workbook = openpyxl.load_workbook(file_path, data_only=True)
    print("Planilhas disponíveis:", workbook.sheetnames)
except FileNotFoundError:
    print("Arquivo não encontrado. Verifique o nome do arquivo e o caminho.")
except Exception as e:
    print(f"Ocorreu um erro ao tentar ler o arquivo: {e}")

