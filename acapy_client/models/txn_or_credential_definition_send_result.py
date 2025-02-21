from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.credential_definition_send_result import CredentialDefinitionSendResult
from ..models.transaction_record import TransactionRecord
from ..types import UNSET, Unset

T = TypeVar("T", bound="TxnOrCredentialDefinitionSendResult")


@attr.s(auto_attribs=True)
class TxnOrCredentialDefinitionSendResult:
    """ """

    sent: Union[Unset, CredentialDefinitionSendResult] = UNSET
    txn: Union[Unset, TransactionRecord] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sent: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sent, Unset):
            sent = self.sent.to_dict()

        txn: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.txn, Unset):
            txn = self.txn.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sent is not UNSET:
            field_dict["sent"] = sent
        if txn is not UNSET:
            field_dict["txn"] = txn

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _sent = d.pop("sent", UNSET)
        sent: Union[Unset, CredentialDefinitionSendResult]
        if isinstance(_sent, Unset):
            sent = UNSET
        else:
            sent = CredentialDefinitionSendResult.from_dict(_sent)

        _txn = d.pop("txn", UNSET)
        txn: Union[Unset, TransactionRecord]
        if isinstance(_txn, Unset):
            txn = UNSET
        else:
            txn = TransactionRecord.from_dict(_txn)

        txn_or_credential_definition_send_result = cls(
            sent=sent,
            txn=txn,
        )

        txn_or_credential_definition_send_result.additional_properties = d
        return txn_or_credential_definition_send_result

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
