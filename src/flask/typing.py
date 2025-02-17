from __future__ import annotations
import typing as t
if t.TYPE_CHECKING:
    from _typeshed.wsgi import WSGIApplication
    from werkzeug.datastructures import Headers
    from werkzeug.sansio.response import Response
ResponseValue = t.Union['Response', str, bytes, t.List[t.Any], t.Mapping[str, t.Any], t.Iterator[str], t.Iterator[bytes]]
HeaderValue = t.Union[str, t.List[str], t.Tuple[str, ...]]
HeadersValue = t.Union['Headers', t.Mapping[str, HeaderValue], t.Sequence[t.Tuple[str, HeaderValue]]]
ResponseReturnValue = t.Union[ResponseValue, t.Tuple[ResponseValue, HeadersValue], t.Tuple[ResponseValue, int], t.Tuple[ResponseValue, int, HeadersValue], 'WSGIApplication']
ResponseClass = t.TypeVar('ResponseClass', bound='Response')
AppOrBlueprintKey = t.Optional[str]
AfterRequestCallable = t.Union[t.Callable[[ResponseClass], ResponseClass], t.Callable[[ResponseClass], t.Awaitable[ResponseClass]]]
BeforeFirstRequestCallable = t.Union[t.Callable[[], None], t.Callable[[], t.Awaitable[None]]]
BeforeRequestCallable = t.Union[t.Callable[[], t.Optional[ResponseReturnValue]], t.Callable[[], t.Awaitable[t.Optional[ResponseReturnValue]]]]
ShellContextProcessorCallable = t.Callable[[], t.Dict[str, t.Any]]
TeardownCallable = t.Union[t.Callable[[t.Optional[BaseException]], None], t.Callable[[t.Optional[BaseException]], t.Awaitable[None]]]
TemplateContextProcessorCallable = t.Union[t.Callable[[], t.Dict[str, t.Any]], t.Callable[[], t.Awaitable[t.Dict[str, t.Any]]]]
TemplateFilterCallable = t.Callable[..., t.Any]
TemplateGlobalCallable = t.Callable[..., t.Any]
TemplateTestCallable = t.Callable[..., bool]
URLDefaultCallable = t.Callable[[str, t.Dict[str, t.Any]], None]
URLValuePreprocessorCallable = t.Callable[[t.Optional[str], t.Optional[t.Dict[str, t.Any]]], None]
ErrorHandlerCallable = t.Union[t.Callable[[t.Any], ResponseReturnValue], t.Callable[[t.Any], t.Awaitable[ResponseReturnValue]]]
RouteCallable = t.Union[t.Callable[..., ResponseReturnValue], t.Callable[..., t.Awaitable[ResponseReturnValue]]]