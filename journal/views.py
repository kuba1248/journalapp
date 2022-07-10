from django.utils import timezone
from django.shortcuts import render
from journal.models import Journal
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


# Создаем представления в этой части кода.

class JournalListView(ListView):
    model = Journal
    template_name = 'journal/journal_list.html'
    context_object_name = 'journal_list'
    success_url = reverse_lazy('journallist')
    paginate_by = 5

class JournalCreateView(CreateView):
    model = Journal
    template_name = 'journal/create_journal_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('journallist')


class JournalUpdateView(UpdateView):
    model = Journal
    template_name = 'journal/update_journal_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('journallist')


class JournalDeleteView(DeleteView):
    model = Journal
    template_name = 'journal/delete_journal_form.html'
    success_url = reverse_lazy('journallist')


class JournalDetailView(DetailView):
    model = Journal
    template_name = 'journal/journal_detail.html'
    fields = ['title', 'description', 'date_created']
    success_url = reverse_lazy('journallist')

    def journal_detail(request, pk):
        journal = get_object_or_404(Journal, pk=pk)

        return render(request, "journal/journal_detail.html")

