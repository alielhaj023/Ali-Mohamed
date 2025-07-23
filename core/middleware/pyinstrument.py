import os
from django.utils.deprecation import MiddlewareMixin
from pyinstrument import Profiler


class PyInstrumentMiddleware(MiddlewareMixin):
    """
    Middleware for profiling Django requests using pyinstrument with
    flag-based control.
    """

    def process_request(self, request):
        """Start profiling if ENABLE_PROFILING is set to True."""
        self.enable_profiling = (
            os.getenv("ENABLE_PROFILING", "False").lower() == "true"
        )

        if self.enable_profiling:
            request.profiler = Profiler()
            request.profiler.start()

    def process_response(self, request, response):
        """Stop profiling and print/save report if profiling was enabled."""
        if self.enable_profiling and hasattr(request, "profiler"):
            request.profiler.stop()

            # Print report to console
            print(request.profiler.output_text(unicode=True, color=True))

            # Optional: Save to a file
            with open("pyinstrument_profile.txt", "a") as f:
                f.write(request.profiler.output_text(unicode=True))

        return response
