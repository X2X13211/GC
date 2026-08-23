from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'cover_image', 'content', 'is_published']

        widgets = {
            'cover_image': forms.ClearableFileInput(attrs={
                'class': 'w-full px-4 py-2 text-sm text-slate-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100',
                'id': 'image-upload-input'
            }),

            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 bg-white text-sm focus:border-slate-500 focus:outline-none',
                'placeholder': 'Введите заголовок поста'
            }),

            'content': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 bg-white text-sm focus:border-slate-500 focus:outline-none',
                'placeholder': 'Введите текст поста',
                'rows': 8,
            }),

            'is_published': forms.CheckboxInput(attrs={
                'class': 'w-4 h-4 mt-1 rounded border-gray-200 bg-gray-100 accent-slate-600 focus:ring-2 focus:ring-blue-500'
            }),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 bg-white text-sm focus:border-slate-500 focus:outline-none',
                'placeholder': 'Написать комментарий...',
                'rows': 3,
            })
        }
        labels = {
            'body': ''
        }