from datetime import datetime

from django.template import Template
from django_components import component


@component.register("countdown")
class Countdown(component.Component):
    template_string = """
        <span
          data-ended-at-timestamp="{{ until.timestamp }}"
          x-data="{
                interval: null,
                init() {
                    this.endTimestamp = parseInt($el.dataset.endedAtTimestamp);
                    this.processCountdown();
                    this.interval = setInterval(() => this.processCountdown(), 1000);
                },
                processCountdown() {
                    const currentTimestamp = Math.floor(Date.now() / 1000)
                    const remainingTime = this.endTimestamp - currentTimestamp;
                    if ($refs.days === undefined && this.interval !== null) {
                        clearInterval(this.interval)
                    } else {
                        $refs.days.innerHTML = Math.floor(remainingTime / 60 / 60 / 24)
                        $refs.hours.innerHTML = Math.floor(remainingTime / 60 / 60) % 24
                        $refs.minutes.innerHTML = Math.floor(remainingTime / 60) % 60
                        $refs.seconds.innerHTML = Math.floor(remainingTime) % 60
                    }
                }
            }"
        >
            <span x-ref="days"></span>j
            <span x-ref="hours"></span>h
            <span x-ref="minutes"></span>ms
            <span x-ref="seconds"></span>s
        </span>
    """

    def get_context_data(self, until: datetime):
        return {
            "until": until,
        }
