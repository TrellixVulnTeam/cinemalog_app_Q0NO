import graphene
from graphene_django.types import DjangoObjectType,ObjectType
from django.views.decorators.csrf import csrf_exempt # use befor defs for security
from cinemalog.models import SendPush
class SendPushType(DjangoObjectType):
    class Meta:
        model=SendPush
#get data (GET_method)
class Query(ObjectType):
    all_sendpush=graphene.List(SendPushType)
    sendpush_detail=graphene.Field(SendPushType,id=graphene.Int())
    def resolve_all_sendpush(self,info,**kwargs):
        return SendPush.objects.all()

    def resolve_sendpush_detail(self,info,id=None,**kwargs):
        if id is not None:
            print('iddddddddddddddd',id)
            return SendPush.objects.get(pk=id)

#create,update,destroy data   (POST PUT DELETE methods)
class SendpushInput(graphene.InputObjectType):
    #id=graphene.ID()
    title=graphene.String()
    content=graphene.String()
    platform_ios=graphene.Boolean()
    platform_android=graphene.Boolean()
    user_id=graphene.Int()


class CreateSendPush(graphene.Mutation):
    class Arguments:
        input=SendpushInput()
    sendpush=graphene.Field(SendPushType)
    def mutate(self,info,input=None,**kwargs):
        sendpush_instance=SendPush(
            title=input.title,
            content=input.content,
            platform_ios=input.platform_ios,
            platform_android=input.platform_android,
            user_id=input.user_id)
        sendpush_instance.save()
        return CreateSendPush(sendpush=sendpush_instance)

class UpdateSendpush(graphene.Mutation):
    class Arguments:
        id=graphene.Int()
        input=SendpushInput()
    
    sendpush=graphene.Field(SendPushType)
    def mutate(self,info,id,input=None,**kwargs):
        sendpush_instance=SendPush.objects.get(pk=id)
        if sendpush_instance:
            sendpush_instance.title=input.title
            sendpush_instance.content=input.content
            sendpush_instance.platform_ios=input.platform_ios
            sendpush_instance.platform_android=input.platform_android
            sendpush_instance.save()
            return UpdateSendpush(sendpush=sendpush_instance)
        return UpdateSendpush(sendpush=None)

class DestroySendPush(graphene.Mutation):
    class Arguments:
        id=graphene.Int()
    sendpush=graphene.Field(SendPushType)
    
    def mutate(self,info,id,**kwargs):
        print('idddddddddddddd',id)
        sendpush_instance=SendPush.objects.get(pk=id)
        if sendpush_instance:
            sendpush_instance.delete()
            return DestroySendPush(sendpush=sendpush_instance)
        return DestroySendPush(sendpush=None)
class Mutation(graphene.ObjectType):
    create_sendpush=CreateSendPush.Field()
    update_sendpush=UpdateSendpush.Field()
    destroy_sendpush=DestroySendPush.Field()


    
