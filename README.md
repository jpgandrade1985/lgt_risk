# lgt_risk
Métricas de Risco dos Fundos da Legatus

---
# Para Criar o Container
Estou usado fedora 40 com podman instalado

Usei o podman para criar o container da seguinte maneira:


 $ podman build -t <container_name> -f Containerfile .


apos o container ser buildado rodei o mesmo como daemon da seguinte maneira


 $ podman run -d --name lgt_risk -p 8501:8501 localhost/<container_name>:latest
Não esqueça de subistuir o nome do container pelo nome que vc usou na build

ex: 


 $ podman build -f Containerfile -t streamlit .

 $ podman run -d --name teste_stream1 -p 8501:8501 localhost/streamlit:latest

