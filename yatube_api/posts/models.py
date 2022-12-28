from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название группы')
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Описание группы')

    def __str__(self):
        return self.title[:15]

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Post(models.Model):
    text = models.TextField(verbose_name='Текст поста')
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор поста'
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True,
        verbose_name='Картинка'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
        verbose_name='Группа'
    )

    def __str__(self):
        return self.text[:15]

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пост'
    )
    text = models.TextField(verbose_name='Текст комментария')
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='follower'
    )
    following = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='following'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("user", "following"),
                name="unique_user_following"
            )
        ]
