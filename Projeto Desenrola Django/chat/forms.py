from django import forms
class MensagemForm(forms.Form):
    texto = forms.CharField(max_length=2000, strip=True, label="Mensagem", widget=forms.Textarea(attrs={"rows":3, "placeholder":"Escreva sua mensagem…", "maxlength":2000}))
