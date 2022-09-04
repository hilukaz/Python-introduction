

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

f = open("demofile2.txt", "r")
print(f.read())


#"r"- Leitura - Valor padrão. Abre um arquivo para leitura, erro se o arquivo não existir (default)

#"a"- Append - Abre um arquivo para anexação, cria o arquivo se não existir

#"w"- Write - Abre um arquivo para escrita, cria o arquivo caso não exista

#"x"- Criar - Cria o arquivo especificado, retorna um erro se o arquivo existir


#"t"- Texto - Valor padrão. Modo de texto (default)

#"b"- Binário - Modo binário (por exemplo, imagens)