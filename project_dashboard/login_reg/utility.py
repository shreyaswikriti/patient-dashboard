from django.contrib.auth import authenticate, login , logout, update_session_auth_hash
from .forms import *
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)

