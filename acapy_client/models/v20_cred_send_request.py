from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.v20_cred_filter import V20CredFilter
from ..models.v20_cred_preview import V20CredPreview
from ..types import UNSET, Unset

T = TypeVar("T", bound="V20CredSendRequest")


@attr.s(auto_attribs=True)
class V20CredSendRequest:
    """ """

    connection_id: str
    filter_: V20CredFilter
    auto_remove: Union[Unset, bool] = UNSET
    comment: Union[Unset, None, str] = UNSET
    credential_preview: Union[Unset, V20CredPreview] = UNSET
    trace: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_id = self.connection_id
        filter_ = self.filter_.to_dict()

        auto_remove = self.auto_remove
        comment = self.comment
        credential_preview: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credential_preview, Unset):
            credential_preview = self.credential_preview.to_dict()

        trace = self.trace

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connection_id": connection_id,
                "filter": filter_,
            }
        )
        if auto_remove is not UNSET:
            field_dict["auto_remove"] = auto_remove
        if comment is not UNSET:
            field_dict["comment"] = comment
        if credential_preview is not UNSET:
            field_dict["credential_preview"] = credential_preview
        if trace is not UNSET:
            field_dict["trace"] = trace

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connection_id = d.pop("connection_id")

        filter_ = V20CredFilter.from_dict(d.pop("filter"))

        auto_remove = d.pop("auto_remove", UNSET)

        comment = d.pop("comment", UNSET)

        _credential_preview = d.pop("credential_preview", UNSET)
        credential_preview: Union[Unset, V20CredPreview]
        if isinstance(_credential_preview, Unset):
            credential_preview = UNSET
        else:
            credential_preview = V20CredPreview.from_dict(_credential_preview)

        trace = d.pop("trace", UNSET)

        v20_cred_send_request = cls(
            connection_id=connection_id,
            filter_=filter_,
            auto_remove=auto_remove,
            comment=comment,
            credential_preview=credential_preview,
            trace=trace,
        )

        v20_cred_send_request.additional_properties = d
        return v20_cred_send_request

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
