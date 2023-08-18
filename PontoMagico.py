import click
import pandas as pd
import os
import datetime
from openpyxl import load_workbook

def identify_batidas(row):
    if isinstance(row, str):
        batidas = row.split(' ')
        return len(batidas)
    return 0

def extract_day_of_week(text):
    if isinstance(text, str):
        parts = text.split(' ')
        if len(parts) > 1:
            return parts[-1]
    return ''

def extract_justificativa(text):
    if isinstance(text, str):
        return text.split(' - ')[-1].strip()
    return ''

def extract_date(text):
    if isinstance(text, str):
        parts = text.split(' ')
        return parts[0]
    return None

def extract_time_columns(row, num_batidas):
    if isinstance(row, str):
        batidas = row.split(' ')
        if len(batidas) == num_batidas:
            return batidas
    return [None] * num_batidas

@click.command()
@click.option('--input', prompt='Caminho da planilha de entrada',
              help='Caminho para a planilha de entrada')
def main(input):
    click.secho("Bem-vindo ao Ponto Mágico!", fg='green')
    
    input = os.path.abspath(input)
    output_folder = os.path.join(os.getcwd(), 'tratamentos')
    
    if not input.endswith('.xlsx'):
        click.secho("O arquivo de entrada deve estar no formato .xlsx.", fg='red')
        return
    
    click.echo(f"Carregando a planilha de {input}...")
    
    try:
        df = pd.read_excel(input, skiprows=5)  # Lê a partir da linha 6
    except Exception as e:
        click.secho(f"Erro ao carregar a planilha: {e}", fg='red')
        return
    
    click.echo("Planilha carregada. Verificando as primeiras linhas...")
    print(df.head(6))  # Exibir as primeiras linhas para depuração

    if 'Data da Marcação' not in df.columns:
        click.secho("A coluna 'Data da Marcação' não foi encontrada na planilha.", fg='red')
        return

    click.echo("Realizando tratamentos nos dados...")

    # Tratamento 1: Separar data e dia da semana
    df['Dia da Semana'] = df['Data da Marcação'].apply(extract_day_of_week)
    df['Data da Marcação'] = df['Data da Marcação'].apply(extract_date)

    # Identificar quantidade de batidas
    df['Quantidade de Batidas'] = df['Marcações'].apply(identify_batidas)

    # Tratamento 2: Separar as batidas em colunas
    max_splits = df['Quantidade de Batidas'].max()
    for i in range(max_splits):
        time_column = f'Batida {i+1}'
        df[time_column] = df['Marcações'].apply(lambda x: x.split(' ')[i] if isinstance(x, str) and len(x.split(' ')) > i else None)

    # Tratamento 4: Limpar justificativa
    df['Justificativa'] = df['Justificativa'].apply(extract_justificativa)

    current_date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output = os.path.join(output_folder, f"nova_planilha_{current_date}.xlsx")
    
    df.drop(columns=['Marcações', 'Quantidade de Batidas'], inplace=True)
    df.to_excel(output, index=False, engine='openpyxl')  # Use o mecanismo 'openpyxl' para garantir compatibilidade com o Excel

    click.secho("Tratamento concluído! A nova planilha foi salva com sucesso.", fg='green')

if __name__ == '__main__':
    main()
