import os
import cProfile
import pstats
import io
from django.utils.deprecation import MiddlewareMixin


class CProfileMiddleware(MiddlewareMixin):
    """
    Middleware for profiling Django requests using cProfile.
    Enables profiling based on environment flags and specific apps.
    """

    def process_request(self, request):
        """Start profiling if enabled and app is in the allowlist."""
        self.enable_profiling = (
            os.getenv("ENABLE_PROFILING", "False").lower() == "true"
        )
        self.profiled_apps = os.getenv("PROFILED_APPS", "").split(",")

        if self.enable_profiling and self._should_profile_request(request):
            self.profiler = cProfile.Profile()
            self.profiler.enable()
        else:
            self.profiler = None

    def process_response(self, request, response):
        """Stop profiling and save results if profiling was enabled."""
        if self.profiler:
            self.profiler.disable()
            result_stream = io.StringIO()
            stats = pstats.Stats(self.profiler, stream=result_stream)
            stats.strip_dirs().sort_stats("cumulative").print_stats(
                20
            )  # Show top 20 functions

            with open("profiling_results.txt", "a") as f:
                f.write(f"\n\nProfiling results for {request.path}:\n")
                f.write(result_stream.getvalue())

            print(result_stream.getvalue())

        return response

    def _should_profile_request(self, request):
        """Check if the request should be profiled based on the app name."""
        app_name = self._extract_app_from_path(request.path)
        return app_name in self.profiled_apps if self.profiled_apps else True

    def _extract_app_from_path(self, path):
        """
        Extracts the first path component to determine the Django app name.
        Example: "/app1/login/" → "app1"
        """
        path_parts = path.strip("/").split("/")
        return path_parts[0] if path_parts else None
