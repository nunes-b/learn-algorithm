"""
Imagine que você está criando uma aplicação de gerenciamento de logística.
A primeira versão vai  lidar apenas com transporte de caminhões
Portanto a maior parte do código vai ficar dentro da classe Caminhão.

Depois de um tempo a sua aplicação se torna escalavél e popular.
Todo os dias você recebe dezenas de solicitações de empresas
de transporte maritmo pra incoporpar a logística maritima na aplicação.

Boa noticia, certo? mas e o codigo?
Atualmente a maior parte do seu codigo é acoplada à classe Caminhão.
Adicionar Navia à aplicação exigiria alterações em toda a base de código.
Além disso, se mais tarde você decididr adicionar outro tipo de transporte
à aplicação, provavelmente precisar fazer todas essas alterações novamente

Como resultado você terá um codigo bastante sujo. Repleto de condicionais que
alteram o comportamento
da aplicação, dependendo da classe de objetos de transporte.

Solução:
O padrão factory method sugere que você substitua chamadas diretas
por chamadas para um metodo fabrica especial, mas esse está sendo chamado de
dentro do metodo fabrica
 Objetos retornados por um metodo fabrica geralmente são chamados de
produtos.
"""
