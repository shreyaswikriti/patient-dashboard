from patient.models import PatientTreatment, PatientAppointment, TreatmentComment
from .models import DoctorProfile
import logging
logger = logging.getLogger(__name__)





def get_treatment_details(request, pk):
	treatment = PatientTreatment.objects.filter(id=pk).first()
	if treatment is None:
		logger.error("Treatment does not exist")
		redirect('error')
	treatments = PatientTreatment.objects.filter(parent_treatment=treatment.id).order_by('-count')
	comments = TreatmentComment.objects.filter(treatment=treatment).order_by('timestamp')
	if comments is None:
		logger.info("No comments available")
	yes = is_treatment_by_loggedin_doc(request, pk)
	context = {'comments':comments, 'treatment':treatment, 'treatments':treatments, 'yes':yes}
	return context



def is_treatment_by_loggedin_doc(request, pk):
	doctor = DoctorProfile.objects.filter(user=request.user).first()
	treatment = PatientTreatment.objects.filter(id=pk).first()
	if doctor.id == treatment.doctor.id:
		return True
	else:
		return False


def edit_treatment_detail(request, count, diagnosis, prescription, treatment_id, patient, doctor):
	PatientTreatment.objects.create(doctor=doctor, parent_treatment=treatment_id, count=count,
		diagnosis=diagnosis, active=True, patient=patient, prescription=prescription)