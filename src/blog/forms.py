from django import Comment, forms


class EmailPostForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(widget=forms.Textarea, required=False)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
