import logging as log
log.basicConfig(level=log.DEBUG,format = '\t -> %(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s', 
                datefmt='%I:%M:%S %p',
                handlers= [
                    log.FileHandler('laboratorio_usuario.log'),
                    log.StreamHandler()
                ]
                )