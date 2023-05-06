from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Question, Comment
from .forms import CommentForm
from taggit.models import Tag
from collections import Counter


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.question = Question.objects.create(
            title='testtitle',
            content='testcontent',
            user=self.user,
            
        )
        self.tag = Tag.objects.create(name='testtag')

        self.comment = Comment.objects.create(
            content='testcomment',
            question=self.question,
        )

        # self.like = Like.objects.create(
        #     user=self.user,
        #     comment=self.comment,
        #     is_like=True,
        # )

        self.question_detail_url = reverse('smb_base:question-detail', args=[str(self.question.id)])
        self.question_create_url = reverse('smb_base:question-create')
        self.question_update_url = reverse('smb_base:question-update', args=[str(self.question.id)])
        self.question_delete_url = reverse('smb_base:question-delete', args=[str(self.question.id)])
        self.comment_detail_url = reverse('smb_base:question-detail', args=[str(self.comment.id)])
        self.add_comment_url = reverse('smb_base:question-comment', args=[str(self.question.id)])

    def test_question_list_view(self):
        response = self.client.get(reverse('smb_base:question-lists'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'smb_base/question_list.html')

    def test_question_list_by_tag_view(self):
        response = self.client.get(reverse('smb_base:question-tag', args=[str(self.question.id),str(self.tag.name)]))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'smb_base/question_list.html')

    def test_question_detail_view(self):
        response = self.client.get(self.question_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'smb_base/question_detail.html')

    def test_question_create_view(self):
        self.client.login(username='testuser', password='testpass')

        response = self.client.post(self.question_create_url, {
            'title': 'testtitle2',
            'content': 'testcontent2',
            'tag': self.tag.id,
        })

        self.assertEquals(response.status_code, 302)
        self.assertTrue(Question.objects.filter(title='testtitle2').exists())

    def test_question_update_view(self):
        self.client.login(username='testuser', password='testpass')

        response = self.client.post(self.question_update_url, {
            'title': 'testtitle3',
            'content': 'testcontent3',
            'tag': self.tag.id,
        })

        self.assertEquals(response.status_code, 302)
        self.assertTrue(Question.objects.filter(title='testtitle3').exists())

    def test_question_delete_view(self):
        self.client.login(username='testuser', password='testpass')

        response = self.client.post(self.question_delete_url)

        self.assertEquals(response.status_code, 302)
        self.assertFalse(Question.objects.filter(title='testtitle').exists())
    


    def test_comment_detail_view(self):

        response = self.client.get(self.comment_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'smb_base/question_detail.html')
            
    # def test_add_comment(self):
    #     form_data = {'text': 'Test Comment'}
    #     response = self.client.post(self.add_comment_url , form_data)

    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response,reverse('smb_base:question-lists'))
    #     self.assertEqual(Comment.objects.count(), 1)
    #     comment = Comment.objects.first()
    #     self.assertEqual(comment.text, 'Test Comment')
    #     self.assertEqual(comment.author, self.user)
    #     self.assertEqual(comment.question, self.question)


# class TagListViewTestCase(TestCase):
#     def setUp(self):
#         Tag.objects.create(name='tag1')
#         Tag.objects.create(name='tag2')

#     def test_tag_list_view(self):
#         response = self.client.get(reverse('smb_base:tag-list'))
#         self.assertEqual(response.status_code, 200)
#         tag_list = Tag.objects.all().order_by('name')
#         self.assertQuerysetEqual(
#             response.context['tag_list'],
#             tag_list,
#             transform=lambda x: x
#         )


class smb_baseUrlTests(TestCase):

    def setUp(self):

        self.client = Client()

        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.question = Question.objects.create(
            title='testtitle',
            content='testcontent',
            user=self.user,
            
        )
        self.tag = Tag.objects.create(name='testtag')

        self.comment = Comment.objects.create(
            content='testcomment',
            question=self.question,
        )

        # self.like = Like.objects.create(
        #     user=self.user,
        #     comment=self.comment,
        #     is_like=True,
        # )

    def test_question_list_url(self):
        response = self.client.get(reverse('smb_base:question-lists'))
        self.assertEqual(response.status_code, 200)

    def test_question_create_url(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('smb_base:question-create'))
        self.assertEqual(response.status_code, 200)

    def test_question_detail_url(self):
        response = self.client.get(reverse('smb_base:question-detail', args=[self.question.pk]))
        self.assertEqual(response.status_code, 200)

    def test_question_update_url(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('smb_base:question-update', args=[self.question.pk]))
        self.assertEqual(response.status_code, 200)

    def test_question_delete_url(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('smb_base:question-delete', args=[self.question.pk]))
        self.assertEqual(response.status_code, 200)

    def test_question_comment_url(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('smb_base:question-comment', args=[self.question.pk]))
        self.assertEqual(response.status_code, 200)

    def test_question_tag_url(self):
        response = self.client.get(reverse('smb_base:question-tag', args=[self.question.pk, self.tag.name]))
        self.assertEqual(response.status_code, 200)

    def test_tag_question_url(self):
        response = self.client.get(reverse('smb_base:tag-question', args=[self.tag.name]))
        self.assertEqual(response.status_code, 200)

    def test_tag_list_url(self):
        response = self.client.get(reverse('smb_base:tag-list'))
        self.assertEqual(response.status_code, 200)

    # def test_like_comment_url(self):
    #     self.client.login(username='testuser', password='testpass')
    #     response = self.client.post(reverse('smb_base:like_post'), {'comment_id': self.comment.pk})
    #     self.assertEqual(response.status_code,200)
