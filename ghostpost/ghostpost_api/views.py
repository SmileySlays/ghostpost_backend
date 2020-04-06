from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from ghostpost.ghostpost_api.serializers import GhostPostSerializer
from ghostpost.ghostpost_api.models import GhostPost

class GhostPostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = GhostPost.objects.all().order_by('-created_date')
    serializer_class = GhostPostSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'])
    def index(request):
        items = GhostPost.objects.order_by('-created_date')
        return render(request, "index.html", {"data": items})

    @action(detail=True, methods=['get'])
    def like(request, pk):
                ghostpost = GhostPost.objects.get(pk=pk)
                ghostpost.likes += 1
                ghostpost.save()
    
    @action(detail=True, methods=['get'])
    def dislike(request, pk):
                ghostpost = GhostPost.objects.get(pk=pk)
                ghostpost.dislikes += 1
                ghostpost.save()
                return HttpResponseRedirect(reverse('homepage'))

    @action(detail=True, methods=['post'])
    def ghostpost_add_view(request):
        html = "generic_form.html"

        if request.method == "POST":
            form = GhostPostAddForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                GhostPost.objects.create(
                    body=data['body'],
                    boast=data['boast']
                )
                return HttpResponseRedirect(reverse("homepage"))

        form = GhostPostAddForm()

        return render(request, html, {'form': form})
