from core.rpc.hola_pb2 import (
    Event as GRPCEvent,
    ReceivableMessageSegment as GRPCReceivableMessageSegment,
    Sender as GRPCSender,
    Reply as GRPCReply,
    Anonymous as GRPCAnonymous,
    Request as GRPCRequest,

    PrivateMessageRequest as GRPCPrivateMessageRequest,
    GroupMessageRequest as GRPCGroupMessageRequest,
    DeleteMsgRequest as GRPCDeleteMsgRequest,
    GetMsgRequest as GRPCRGetMsgRequest,
    SendGroupForwardMsgRequest as GRPCSendGroupForwardMsgRequest,
    SendPrivateForwardMsgRequest as GRPCSendPrivateForwardMsgRequest,

    PrivateMessageResult as GRPCPrivateMessageResult,
    GroupMessageResult as GRPCGroupMessageResult,
    DeleteMsgResult as GRPCDeleteMsgResult,
    GetMsgResult as GRPCGetMsgResult,
    SendGroupForwardMsgResult as GRPCSendGroupForwardMsgResult,
    SendPrivateForwardMsgResult as GRPCSendPrivateForwardMsgResult,

)
