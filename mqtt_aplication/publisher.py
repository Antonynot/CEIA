import paho.mqtt.client as mqtt


mqtt_client = mqtt.Client('meu_publisher')
mqtt_client.connect(host="test.mosquitto.org", port=1883)
mqtt_client.publish(topic="/minhasMensagens", payload='{ "Tensao": "20V" }')

print('acabou')