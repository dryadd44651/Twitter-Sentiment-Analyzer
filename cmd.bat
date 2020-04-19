cd E:\kafka_2.11-2.4.1\bin\windows
E:\

start .\zookeeper-server-start ..\..\config\zookeeper.properties

start .\kafka-server-start ..\..\config\server.properties

start .\kafka-topics --list --zookeeper localhost:2181

cd E:\

start .\elasticsearch-7.6.1\bin\elasticsearch

start .\kibana-7.6.1-windows-x86_64\bin\kibana