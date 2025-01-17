# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from pysnap import Snapshot


snapshots = Snapshot()

snapshots['TestCodaClient.test_get_daemon_status 1'] = [
    (
        (
            'http://localhost:8304/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': 'query { daemonStatus { numAccounts blockchainLength uptimeSecs ledgerMerkleRoot stateHash peers userCommandsSent runSnarkWorker proposePubkeys consensusTimeNow consensusTimeBestTip consensusMechanism confDir commitId consensusConfiguration { delta k c cTimesK slotsPerEpoch slotDuration epochDuration acceptableNetworkDelay } } }'
            }
        }
    ,)
]

snapshots['TestCodaClient.test_get_daemon_version 1'] = [
    (
        (
            'http://localhost:8304/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': '{ version }'
            }
        }
    ,)
]

snapshots['TestCodaClient.test_get_wallets 1'] = [
    (
        (
            'http://localhost:8304/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': '{ ownedWallets { publicKey } }'
            }
        }
    ,)
]

snapshots['TestCodaClient.test_get_current_snark_worker 1'] = [
    (
        (
            'http://localhost:8304/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': '{ currentSnarkWorker{ key fee } }'
            }
        }
    ,)
]

snapshots['TestCodaClient.test_get_sync_status 1'] = [
    (
        (
            'http://localhost:8304/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': '{ syncStatus }'
            }
        }
    ,)
]

snapshots['TestCodaClient.test_set_current_snark_worker 1'] = [
    (
        (
            'http://localhost:8304/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': '{ syncStatus }'
            }
        }
    ,)
]

snapshots['TestCodaClient.test_send_payment 1'] = [
    (
        (
            'http://localhost:8304/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': 'mutation($from:PublicKey!, $to:PublicKey!, $amount:UInt64!, $fee:UInt64!, $memo:String){ sendPayment(input: { from:$from, to:$to, amount:$amount, fee:$fee, memo:$memo }) { payment { id, isDelegation, nonce, from, to, amount, fee, memo } } }',
                'variables': {
                    'amount': 'amount',
                    'fee': 'fee',
                    'from': 'from_pk',
                    'memo': 'memo',
                    'to': 'to_pk'
                }
            }
        }
    ,)
]

snapshots['TestCodaClient.test_get_wallet 1'] = [
    (
        (
            'http://localhost:8304/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': 'query($publicKey:PublicKey!){ wallet(publicKey:$publicKey) { publicKey balance { total unknown } nonce receiptChainHash delegate votingFor stakingActive privateKeyPath } }',
                'variables': {
                    'publicKey': 'pk'
                }
            }
        }
    ,)
]

snapshots['TestCodaClient.test_create_wallet_no_args 1'] = [
    (
        (
            'http://localhost:8304/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': 'mutation{ addWallet { publicKey } }'
            }
        }
    ,)
]
