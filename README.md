# Johnny-Answers-Session05

colcone build
source install/setup.bash 
mkdir src
cd src 
ros2 pkg create --build-type ament_python temperature_monitor

1) temperature publishes on topic temperature 
2) thershold checks topic temperature, and send alert if above threshold on topic alert_trigger
3) alert_publisher check if there is an alert on topic alert_trigger, and publishes an alert on topic alert

used timer to publish random temperatures.
used spin to keep the node running.