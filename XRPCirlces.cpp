#include <xrp_bot.h>

// Constants
const int LEFT_SPEED = 50;    // Percent (0–100)
const int RIGHT_SPEED = 70;   // Slightly faster for the outer wheel
const int CIRCLE_TIME = 10000; // Run time in milliseconds (10 sec)

void setup() {
  // Initialize the XRP robot
  xrp_init();
}

void loop() {
  // Move in a circle
  xrp_set_motor_speed(LEFT_SPEED, RIGHT_SPEED);
  
  delay(CIRCLE_TIME); // Move in a circle for 10 seconds

  // Stop
  xrp_set_motor_speed(0, 0);

  while (true) {
    // Keep robot stopped forever
  }
}
