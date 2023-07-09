from colorama import Fore, Back, Style
def remover_emails_repetidos(lista_emails):
    emails_unicos = list(set(lista_emails))
    emails_removidos = len(lista_emails) - len(emails_unicos)
    return emails_unicos, emails_removidos


lista_emails = ['']
emails_unicos, emails_removidos = remover_emails_repetidos(lista_emails)

#print(emails_unicos)
print('\n'.join([f"{email}" for email in lista_emails]))
print(f'Quantidade de emails removidos: {Back.RED}{Fore.WHITE}  {emails_removidos}  {Style.RESET_ALL}')
