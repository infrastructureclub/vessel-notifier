# What's this?

This is a bot that:

* monitors vessels in a defined geographic area, using the AISHub API
* keeps a log of the last seen date of each vessel (keyed by MMSI)
* posts a notification to a Slack channel when it spots a vessel that's never been to that are before, or last visited before a configurable timeout

It's configured to run once every hour using GitHub Actions, and commits its database of vessels back to GitHub, so it needs no additional infrastructure to run.

# Dependencies

If you want to deploy your own bot, you'll need:

* An [AISHub API key](https://www.aishub.net/api) (which is normally only available if you run an AIS receiver and [contribute data](https://www.aishub.net/join-us)
* A Slack channel and [webhook set up](https://api.slack.com/messaging/webhooks) for posting notifications
