# Status Page

## About

This is a status page that reflects the health of the platform and that shows information about a ongoing outage.

The three different status reflected are:
 - Uptime (the platform is healthy)
 - Partial degradation (the platform is having some issues)
 - Downtime (the platform is down)

This status page has two different modes: automatic and manual:

- Automatic: The automatic mode feeds from existing metrics that are generated every minute.
- Manual: The manual mode allows a user to update the status of the platform with a manual message through a interactive web interface where the user can write the message and all the metadata related with the message.
         
## Installation

- Download and install [Vagrant](https://www.vagrantup.com/) for your platform.
- Download and install [VirtualBox](https://www.virtualbox.org/) for your platform.

- Clone the repository 
	`git clone git@github.com:csubira/status-page.git`
	`cd status-page`
- Run `vagrant up`

- Open in your browser 
	`http://0.0.0.0:5000/status-page`

## Play with it

- In Automatic mode you can see the latest updates from the service status
- If you click to change mode to Manual, an additional button appears nes to last status. 
A new status can be manually added filling the form.
Note: While manual mode is active, there is not any automatic update registered.
Once the automatic mode is restored, the regular of service status feed is resumed.

_All status are stored in a log in order to be available in the future_ 