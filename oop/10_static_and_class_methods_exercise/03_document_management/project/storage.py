from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:

    def __init__(self):
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    @staticmethod
    def add_instance(collection, instance):
        if instance not in collection:
            collection.append(instance)

    def add_category(self, category: Category):
        self.add_instance(self.categories, category)

    def add_topic(self, topic: Topic):
        self.add_instance(self.topics, topic)

    def add_document(self, document: Document):
        self.add_instance(self.documents, document)

    @staticmethod
    def get_object_by_id(objects, object_id):
        return next((o for o in objects if o.id == object_id), None)

    @staticmethod
    def edit_instance(instances, instance_id: int, *args):
        cur_instance = Storage.get_object_by_id(instances, instance_id)
        if cur_instance:
            cur_instance.edit(*args)

    @staticmethod
    def delete_instance(instances, instance_id):
        cur_instance = Storage.get_object_by_id(instances, instance_id)
        if cur_instance:
            instances.remove(cur_instance)

    def edit_category(self, category_id: int, new_name: str):
        self.edit_instance(self.categories, category_id, new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        self.edit_instance(self.topics, topic_id, new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        self.edit_instance(self.documents, document_id, new_file_name)

    def delete_category(self, category_id):
        self.delete_instance(self.categories, category_id)

    def delete_topic(self, topic_id):
        self.delete_instance(self.topics, topic_id)

    def delete_document(self, document_id):
        self.delete_instance(self.documents, document_id)

    def get_document(self, document_id):
        return self.get_object_by_id(self.documents, document_id)

    def __repr__(self):
        doc_details = "\n".join([d.__repr__() for d in self.documents])
        return doc_details

