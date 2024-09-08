# WEBSITE-MONITORING-AND-RECOVERY
Certainly! Here's a README without the Bash script commands:

---

# Website Monitoring and Recovery

## Overview

This project provides a comprehensive system for monitoring website availability, sending notifications when downtime is detected, and automatically recovering from application failures. It uses Python, Linode, Docker, and Linux to implement these functionalities.

## Components

### 1. Server Setup on Linode

**Purpose:** Deploy a virtual server to host Docker and run monitoring scripts.

- **Create Linode VPS:** 
  - Sign up or log in to Linode.
  - Create an instance with a Linux distribution of your choice (e.g., Ubuntu).
- **Access the VPS:** 
  - Connect to your Linode instance using SSH to configure and manage the server.

### 2. Docker Installation and Container Setup

**Purpose:** Install Docker on the server and run a container that simulates a web service.

- **Install Docker:** 
  - Follow the official Docker documentation to install Docker on your Linode server.
- **Run Container:** 
  - Deploy a Docker container (e.g., Nginx) to serve as a test web service.

### 3. Website Monitoring with Python

**Purpose:** Develop a Python script to check the availability of a website by validating its HTTP response.

- **Script: `monitor_website.py`**
  - Utilizes the `requests` library to make HTTP requests.
  - Verifies the status code of the website to determine if it is up or down.

### 4. Email Notification for Downtime

**Purpose:** Implement a Python script to send email notifications when the website is detected as down.

- **Script: `notify_email.py`**
  - Uses `smtplib` to send emails through an SMTP server.
  - Requires configuration of SMTP settings, such as server address and authentication details.

### 5. Automatic Restart of Application and Server

**Purpose:** Develop a Python script to automatically restart the Docker container if the website is detected as down.

- **Script: `restart_application.py`**
  - Continuously monitors the website and restarts the Docker container if it is down.

## Installation

1. **Clone the Repository:**
   - Obtain the project files by cloning the repository from GitHub.
   - Navigate into the repository directory to access the scripts and configuration files.

2. **Set Up Linode Server:**
   - Create and configure a Linode VPS according to your needs.
   - Install Docker and run a test container to simulate a web service.

3. **Configure and Run Scripts:**
   - Ensure Python 3 is installed on your server.
   - Install any required Python libraries (e.g., `requests`, `smtplib`).
   - Update the Python scripts with your email credentials and SMTP server details.
   - Execute the monitoring, notification, and recovery scripts as needed to ensure functionality.

## Usage

- **Monitor Website:** 
  Run the `monitor_website.py` script to check the website’s availability.
- **Send Notifications:** 
  Execute the `notify_email.py` script to send email alerts if downtime is detected.
- **Automatic Recovery:** 
  Use the `restart_application.py` script to automatically restart the Docker container in case of website downtime.

