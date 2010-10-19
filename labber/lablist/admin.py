from labber.lablist.models import ResearchTopic
from labber.lablist.models import Publication
from labber.lablist.models import Sponsor

from labber.lablist.models import LabMember
from labber.lablist.models import Professor, PostDoc, GradStudent, UnderGrad


from django.contrib import admin

admin.site.register(ResearchTopic)
admin.site.register(Publication)
admin.site.register(Sponsor)