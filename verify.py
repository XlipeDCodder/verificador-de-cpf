import pandas as pd
from validate_docbr import CPF

def verificar_cpfs_final(nome_arquivo_entrada, nome_arquivo_saida):
    """
    Script definitivo que:
    1. Preenche todos os CPFs com zeros à esquerda para garantir 11 dígitos.
    2. Valida o CPF JÁ FORMATADO.
    3. Salva o arquivo de saída forçando a formatação da coluna de CPF como TEXTO
       para que o Excel não remova os zeros à esquerda.
    """
    try:
        
        df = pd.read_excel(nome_arquivo_entrada, dtype=str)
        df.columns = df.columns.str.strip()

        coluna_cpf = 'CPF'
        coluna_status = 'STATUS DE VALIDADE'
        
        
        if coluna_status not in df.columns:
            df[coluna_status] = ''
        df[coluna_status] = df[coluna_status].fillna('')


        cpf_validator = CPF()

        
        for index, row in df.iterrows():
            cpf_value = row[coluna_cpf]

            if pd.isna(cpf_value) or str(cpf_value).strip() == '':
                df.loc[index, coluna_status] = 'Não informado'
                continue

           
            
            cpf_formatado = str(cpf_value).strip().zfill(11)

            
            df.loc[index, coluna_cpf] = cpf_formatado

            
            if cpf_validator.validate(cpf_formatado):
                df.loc[index, coluna_status] = 'Verificado'
            else:
                df.loc[index, coluna_status] = 'Inválido'
        
        
        print("Processamento concluído. Salvando arquivo com formatação de texto...")

        
        with pd.ExcelWriter(nome_arquivo_saida, engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name='Planilha1', index=False)

           
            workbook  = writer.book
            worksheet = writer.sheets['Planilha1']

            
            formato_texto = workbook.add_format({'num_format': '@'})

            
            
            
            worksheet.set_column('A:A', 20, formato_texto)
        
        print(f"Arquivo '{nome_arquivo_saida}' salvo com sucesso! A coluna de CPF está formatada como Texto.")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo_entrada}' não foi encontrado.")
    except KeyError as e:
        print(f"Erro: A coluna {e} não foi encontrada.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


# --- EXECUÇÃO ---
if __name__ == "__main__":
    
    arquivo_entrada = 'NIS_DepPrimPasso_CPF_Cadunico.xlsx' 
    
    arquivo_saida = 'PLANILHA_VALIDADA_FINAL.xlsx'
    
    verificar_cpfs_final(arquivo_entrada, arquivo_saida)