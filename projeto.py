import flet as ft
import time

def main(pagina):
    titulo = ft.Text('Hashzap')
    pagina.add(titulo)
    
    def enviar_mensagem_tunel(mensagem):
        # Executar tudo para todos os usuarios
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()
        pass

    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    
    def enviar_mensagem(evento):
        hora_da_mensagem = time.strftime("%H:%M:%S", time.localtime())
        mensagem = f'{caixa_nome.value.capitalize()} {hora_da_mensagem}: {campo_enviar_mensagem.value}'
        pagina.pubsub.send_all(mensagem)
        campo_enviar_mensagem.value = ''
        pagina.update()

    campo_enviar_mensagem = ft.TextField(label='Digite aqui sua mensagem...', on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)

    chat = ft.Column()
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])


    def entrar_chat(evento):
        popup.open = False
        pagina.remove(titulo)
        pagina.remove(botao)
        pagina.add(chat)
        pagina.add(linha_enviar)
        nome_usuario = caixa_nome.value.capitalize()
        mensagem = f'{nome_usuario} entrou no chat'
        texto_mensagem = ft.Text()
        pagina.pubsub.send_all(mensagem)
        chat.controls.append(texto_mensagem)
        pagina.update()
        

    titulo_popup = ft.Text('Bem Vindo ao Hashzap!')
    caixa_nome = ft.TextField(label='Digite seu nome...', on_submit=entrar_chat)
    botao_popup = ft.ElevatedButton('Entrar no Chat', on_click=entrar_chat)

    popup = ft.AlertDialog(
                            title=titulo_popup,
                            content=caixa_nome,
                            actions=[botao_popup]
                        )

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
    
    
    botao = ft.ElevatedButton('Iniciar Chat', on_click=abrir_popup)
    pagina.add(botao)

    pagina.update()

ft.app(main, view=ft.WEB_BROWSER)

