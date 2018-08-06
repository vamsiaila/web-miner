"""Connects the use case with the response object

Returns:
    class: For processing arxiv document list and apply the filtering on a repo
"""

from webminer.interface_adapters import use_case as uc
from webminer.interface_adapters import response_object as res


class ArxivDocumentListUseCase(uc.UseCase):
    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_object):
        arxiv_documents = self.repo.list(filters=request_object.filters)
        return res.ResponseSuccess(arxiv_documents)