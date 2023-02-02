def recorte(imagen,limites,ancho,alto = 4):

    info=imagen.get_rect()
    an_img=info[2]
    al_img=info[3]
    al_corte=al_img/alto
    an_corte=an_img/ancho
    '''recorte de los usuarios'''
    k=0
    filas = []
    for j in limites:
      fila = []
      for i in range(j):
          cuadro=imagen.subsurface(i*an_corte,k*al_corte,an_corte,al_corte)
          fila.append(cuadro)
      k+=1
      filas.append(fila)
    return filas
