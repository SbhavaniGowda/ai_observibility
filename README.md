<!-- chmod +x scripts/setup.sh
chmod +x scripts/cleanup.sh


eval $(minikube docker-env)

docker build -t ai-service docker/ai-service
docker build -t mock-service docker/mock-service

kubectl apply -f kubernetes/namespace.yaml
kubectl apply -f kubernetes/ai-service.yaml
kubectl apply -f kubernetes/mock-service.yaml

kubectl apply -f kubernetes/alertmanager-secret.yaml
kubectl apply -f kubernetes/alertmanager.yaml
kubectl apply -f kubernetes/prometheus-rules.yaml
kubectl apply -f kubernetes/servicemonitor.yaml
kubectl apply -f kubernetes/grafana-dashboard-cm.yaml -->


 kubectl get servicemonitor -n ai-obs -o yaml
apiVersion: v1
items:
- apiVersion: monitoring.coreos.com/v1
  kind: ServiceMonitor
  metadata:
    annotations:
      kubectl.kubernetes.io/last-applied-configuration: |
        {"apiVersion":"monitoring.coreos.com/v1","kind":"ServiceMonitor","metadata":{"annotations":{},"labels":{"team":"ai"},"name":"ai-service-monitor","namespace":"ai-obs"},"spec":{"endpoints":[{"interval":"5s","path":"/metrics","port":"http"}],"namespaceSelector":{"matchNames":["ai-obs"]},"selector":{"matchLabels":{"app":"ai-service"}}}}
    creationTimestamp: "2026-01-06T06:08:48Z"
    generation: 1
    labels:
      team: ai
    name: ai-service-monitor
    namespace: ai-obs
    resourceVersion: "144517"
    uid: 3d3fb595-6c5e-4eb2-a883-bbcd94496e06
  spec:
    endpoints:
    - interval: 5s
      path: /metrics
      port: http
    namespaceSelector:
      matchNames:
      - ai-obs
    selector:
      matchLabels:
        app: ai-service
- apiVersion: monitoring.coreos.com/v1
  kind: ServiceMonitor
  metadata:
    annotations:
      meta.helm.sh/release-name: monitoring
      meta.helm.sh/release-namespace: ai-obs
    creationTimestamp: "2026-01-06T05:55:13Z"
    generation: 1
    labels:
      app.kubernetes.io/instance: monitoring
      app.kubernetes.io/managed-by: Helm
      app.kubernetes.io/name: grafana
      app.kubernetes.io/version: 12.3.1
      helm.sh/chart: grafana-10.5.1
    name: monitoring-grafana
    namespace: ai-obs
    resourceVersion: "143578"
    uid: 7e4cc00b-0c42-4c57-beb8-4ffc98354438
  spec:
    endpoints:
    - honorLabels: true
      path: /metrics
      port: http-web
      scheme: http
      scrapeTimeout: 30s
    jobLabel: monitoring
    namespaceSelector:
      matchNames:
      - ai-obs
    selector:
      matchLabels:
        app.kubernetes.io/instance: monitoring
        app.kubernetes.io/name: grafana
- apiVersion: monitoring.coreos.com/v1
  kind: ServiceMonitor
  metadata:
    annotations:
      meta.helm.sh/release-name: monitoring
      meta.helm.sh/release-namespace: ai-obs
    creationTimestamp: "2026-01-06T05:55:13Z"
    generation: 1
    labels:
      app: kube-prometheus-stack-alertmanager
      app.kubernetes.io/instance: monitoring
      app.kubernetes.io/managed-by: Helm
      app.kubernetes.io/part-of: kube-prometheus-stack
      app.kubernetes.io/version: 80.11.0
      chart: kube-prometheus-stack-80.11.0
      heritage: Helm
      release: monitoring
    name: monitoring-kube-prometheus-alertmanager
    namespace: ai-obs
    resourceVersion: "143576"
    uid: e95294bb-eff3-4cb8-ade2-357dc6752c8d
  spec:
    endpoints:
    - enableHttp2: true
      path: /metrics
      port: http-web
    - path: /metrics
      port: reloader-web
    namespaceSelector:
      matchNames:
      - ai-obs
    selector:
      matchLabels:
        app: kube-prometheus-stack-alertmanager
        release: monitoring
        self-monitor: "true"
- apiVersion: monitoring.coreos.com/v1
  kind: ServiceMonitor
  metadata:
    annotations:
      meta.helm.sh/release-name: monitoring
      meta.helm.sh/release-namespace: ai-obs
    creationTimestamp: "2026-01-06T05:55:13Z"
    generation: 1
    labels:
      app: kube-prometheus-stack-apiserver
      app.kubernetes.io/instance: monitoring
      app.kubernetes.io/managed-by: Helm
      app.kubernetes.io/part-of: kube-prometheus-stack
      app.kubernetes.io/version: 80.11.0
      chart: kube-prometheus-stack-80.11.0
      heritage: Helm
      release: monitoring
    name: monitoring-kube-prometheus-apiserver
    namespace: ai-obs
    resourceVersion: "143577"
    uid: a6bfffc0-8e12-4932-a863-c8f5c696ee8b
  spec:
    endpoints:
    - bearerTokenFile: /var/run/secrets/kubernetes.io/serviceaccount/token
      metricRelabelings:
      - action: drop
        regex: (etcd_request|apiserver_request_slo|apiserver_request_sli|apiserver_request)_duration_seconds_bucket;(0\.15|0\.2|0\.3|0\.35|0\.4|0\.45|0\.6|0\.7|0\.8|0\.9|1\.25|1\.5|1\.75|2|3|3\.5|4|4\.5|6|7|8|9|15|20|40|45|50)(\.0)?
        sourceLabels:
        - __name__
        - le
      port: https
      scheme: https
      tlsConfig:
        caFile: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
        insecureSkipVerify: false
        serverName: kubernetes
    jobLabel: component
    namespaceSelector:
      matchNames:
      - default
    selector:
      matchLabels:
        component: apiserver
        provider: kubernetes
- apiVersion: monitoring.coreos.com/v1
  kind: ServiceMonitor
  metadata:
    annotations:
      meta.helm.sh/release-name: monitoring
      meta.helm.sh/release-namespace: ai-obs
    creationTimestamp: "2026-01-06T05:55:13Z"
    generation: 1
    labels:
      app: kube-prometheus-stack-coredns
      app.kubernetes.io/instance: monitoring
      app.kubernetes.io/managed-by: Helm
      app.kubernetes.io/part-of: kube-prometheus-stack
      app.kubernetes.io/version: 80.11.0
      chart: kube-prometheus-stack-80.11.0
      heritage: Helm
      release: monitoring
    name: monitoring-kube-prometheus-coredns
    namespace: ai-obs
    resourceVersion: "143573"
    uid: 6672fdeb-783d-43f6-830e-9db7fbfa95e3
  spec:
    endpoints:
    - bearerTokenFile: /var/run/secrets/kubernetes.io/serviceaccount/token
      port: http-metrics
    jobLabel: jobLabel
    namespaceSelector:
      matchNames:
      - kube-system
    selector:
      matchLabels:
        app: kube-prometheus-stack-coredns
        release: monitoring
- apiVersion: monitoring.coreos.com/v1
  kind: ServiceMonitor
  metadata:
    annotations:
      meta.helm.sh/release-name: monitoring
      meta.helm.sh/release-namespace: ai-obs
    creationTimestamp: "2026-01-06T05:55:13Z"
    generation: 1
    labels:
      app: kube-prometheus-stack-kube-controller-manager
      app.kubernetes.io/instance: monitoring
      app.kubernetes.io/managed-by: Helm
      app.kubernetes.io/part-of: kube-prometheus-stack
      app.kubernetes.io/version: 80.11.0
      chart: kube-prometheus-stack-80.11.0
      heritage: Helm
      release: monitoring
    name: monitoring-kube-prometheus-kube-controller-manager
    namespace: ai-obs
    resourceVersion: "143571"
    uid: 08ed911b-d529-44c4-b5ca-2b7edf125424
  spec:
    endpoints:
    - bearerTokenFile: /var/run/secrets/kubernetes.io/serviceaccount/token
      port: http-metrics
      scheme: https
      tlsConfig:
        caFile: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
        insecureSkipVerify: true
    jobLabel: jobLabel
    namespaceSelector:
      matchNames:
      - kube-system
    selector:
      matchLabels:
        app: kube-prometheus-stack-kube-controller-manager
        release: monitoring
- apiVersion: monitoring.coreos.com/v1
  kind: ServiceMonitor
  metadata:
    annotations:
      meta.helm.sh/release-name: monitoring
      meta.helm.sh/release-namespace: ai-obs
    creationTimestamp: "2026-01-06T05:55:13Z"
    generation: 1
    labels:
      app: kube-prometheus-stack-kube-etcd
      app.kubernetes.io/instance: monitoring
      app.kubernetes.io/managed-by: Helm
      app.kubernetes.io/part-of: kube-prometheus-stack
      app.kubernetes.io/version: 80.11.0
      chart: kube-prometheus-stack-80.11.0
      heritage: Helm
      release: monitoring
    name: monitoring-kube-prometheus-kube-etcd
    namespace: ai-obs
    resourceVersion: "143575"
    uid: 618ea6c6-ff49-4bc8-833d-c6f378016dce
  spec:
    endpoints:
    - bearerTokenFile: /var/run/secrets/kubernetes.io/serviceaccount/token
      port: http-metrics
    jobLabel: jobLabel
    namespaceSelector:
      matchNames:
      - kube-system
    selector:
      matchLabels:
        app: kube-prometheus-stack-kube-etcd
        release: monitoring
- apiVersion: monitoring.coreos.com/v1
  kind: ServiceMonitor
  metadata:
    annotations:
      meta.helm.sh/release-name: monitoring
      meta.helm.sh/release-namespace: ai-obs
    creationTimestamp: "2026-01-06T05:55:13Z"
    generation: 1
    labels:
      app: kube-prometheus-stack-kube-proxy
      app.kubernetes.io/instance: monitoring
      app.kubernetes.io/managed-by: Helm
      app.kubernetes.io/part-of: kube-prometheus-stack
      app.kubernetes.io/version: 80.11.0
      chart: kube-prometheus-stack-80.11.0
      heritage: Helm
      release: monitoring
    name: monitoring-kube-prometheus-kube-proxy
    namespace: ai-obs
    resourceVersion: "143581"
    uid: 1b0b1cda-b710-4912-935e-f47e1e6b73ba
  spec:
    endpoints:
    - bearerTokenFile: /var/run/secrets/kubernetes.io/serviceaccount/token
      port: http-metrics
    jobLabel: jobLabel
    namespaceSelector:
      matchNames:
      - kube-system
    selector:
      matchLabels:
        app: kube-prometheus-stack-kube-proxy
        release: monitoring
- apiVersion: monitoring.coreos.com/v1
  kind: ServiceMonitor
  metadata:
    annotations:
      meta.helm.sh/release-name: monitoring
      meta.helm.sh/release-namespace: ai-obs
    creationTimestamp: "2026-01-06T05:55:13Z"
    generation: 1
    labels:
      app: kube-prometheus-stack-kube-scheduler
      app.kubernetes.io/instance: monitoring
      app.kubernetes.io/managed-by: Helm
      app.kubernetes.io/part-of: kube-prometheus-stack
      app.kubernetes.io/version: 80.11.0
      chart: kube-prometheus-stack-80.11.0
      heritage: Helm
      release: monitoring
    name: monitoring-kube-prometheus-kube-scheduler
    namespace: ai-obs
    resourceVersion: "143579"
    uid: d3e41cf1-a6f8-45e7-b247-205d75fb5314
  spec:
    endpoints:
    - bearerTokenFile: /var/run/secrets/kubernetes.io/serviceaccount/token
      port: http-metrics
      scheme: https
      tlsConfig:
        caFile: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
        insecureSkipVerify: true
    jobLabel: jobLabel
    namespaceSelector:
      matchNames:
      - kube-system
    selector:
      matchLabels:
        app: kube-prometheus-stack-kube-scheduler
        release: monitoring
- apiVersion: monitoring.coreos.com/v1
  kind: ServiceMonitor
  metadata:
    annotations:
      meta.helm.sh/release-name: monitoring
      meta.helm.sh/release-namespace: ai-obs
    creationTimestamp: "2026-01-06T05:55:13Z"
    generation: 1
    labels:
      app: kube-prometheus-stack-kubelet
      app.kubernetes.io/instance: monitoring
      app.kubernetes.io/managed-by: Helm
      app.kubernetes.io/part-of: kube-prometheus-stack
      app.kubernetes.io/version: 80.11.0
      chart: kube-prometheus-stack-80.11.0
      heritage: Helm
      release: monitoring
    name: monitoring-kube-prometheus-kubelet
    namespace: ai-obs
    resourceVersion: "143582"
    uid: a998a77a-aa90-4c83-b553-d01ee4606840
  spec:
    attachMetadata:
      node: false
    endpoints:
    - bearerTokenFile: /var/run/secrets/kubernetes.io/serviceaccount/token
      honorLabels: true
      honorTimestamps: true
      metricRelabelings:
      - action: drop
        regex: (csi_operations|storage_operation_duration)_seconds_bucket;(0.25|2.5|15|25|120|600)(\.0)? 
        sourceLabels:
        - __name__
        - le
      port: https-metrics
      relabelings:
      - action: replace
        sourceLabels:
        - __metrics_path__
        targetLabel: metrics_path
      scheme: https
      tlsConfig:
        caFile: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
        insecureSkipVerify: true
    - bearerTokenFile: /var/run/secrets/kubernetes.io/serviceaccount/token
      honorLabels: true
      honorTimestamps: true
      interval: 10s
      metricRelabelings:
      - action: drop
        regex: container_cpu_(cfs_throttled_seconds_total|load_average_10s|system_seconds_total|user_seconds_total)
        sourceLabels:
        - __name__
      - action: drop
        regex: container_fs_(io_current|io_time_seconds_total|io_time_weighted_seconds_total|reads_merged_total|sector_reads_total|sector_writes_total|writes_merged_total)
        sourceLabels:
        - __name__
      - action: drop
        regex: container_memory_(mapped_file|swap)
        sourceLabels:
        - __name__
      - action: drop
        regex: container_(file_descriptors|tasks_state|threads_max)
        sourceLabels:
        - __name__
      - action: drop
        regex: container_memory_failures_total;hierarchy
        sourceLabels:
        - __name__
        - scope
      - action: drop
        regex: container_network_.*;(cali|cilium|cni|lxc|nodelocaldns|tunl).*
        sourceLabels:
        - __name__
        - interface
      - action: drop
        regex: container_spec.*
        sourceLabels:
        - __name__
      - action: drop
        regex: .+;
        sourceLabels:
        - id
        - pod
      path: /metrics/cadvisor
      port: https-metrics
      relabelings:
      - action: replace
        sourceLabels:
        - __metrics_path__
        targetLabel: metrics_path
      scheme: https
      tlsConfig:
        caFile: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
        insecureSkipVerify: true
      trackTimestampsStaleness: true
    - bearerTokenFile: /var/run/secrets/kubernetes.io/serviceaccount/token
      honorLabels: true
      honorTimestamps: true
      path: /metrics/probes
      port: https-metrics
      relabelings:
      - action: replace
        sourceLabels:
        - __metrics_path__
        targetLabel: metrics_path
      scheme: https
      tlsConfig:
        caFile: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
        insecureSkipVerify: true
    jobLabel: k8s-app
    namespaceSelector:
      matchNames:
      - kube-system
    selector:
      matchLabels:
        app.kubernetes.io/name: kubelet
        k8s-app: kubelet
- apiVersion: monitoring.coreos.com/v1
  kind: ServiceMonitor
  metadata:
    annotations:
      meta.helm.sh/release-name: monitoring
      meta.helm.sh/release-namespace: ai-obs
    creationTimestamp: "2026-01-06T05:55:13Z"
    generation: 1
    labels:
      app: kube-prometheus-stack-operator
      app.kubernetes.io/component: prometheus-operator
      app.kubernetes.io/instance: monitoring
      app.kubernetes.io/managed-by: Helm
      app.kubernetes.io/name: kube-prometheus-stack-prometheus-operator
      app.kubernetes.io/part-of: kube-prometheus-stack
      app.kubernetes.io/version: 80.11.0
      chart: kube-prometheus-stack-80.11.0
      heritage: Helm
      release: monitoring
    name: monitoring-kube-prometheus-operator
    namespace: ai-obs
    resourceVersion: "143580"
    uid: ac44fb6c-a4a0-4541-a4af-83a5442a91fd
  spec:
    endpoints:
    - honorLabels: true
      port: https
      scheme: https
      tlsConfig:
        ca:
          secret:
            key: ca
            name: monitoring-kube-prometheus-admission
            optional: false
        serverName: monitoring-kube-prometheus-operator
    namespaceSelector:
      matchNames:
      - ai-obs
    selector:
      matchLabels:
        app: kube-prometheus-stack-operator
        release: monitoring
- apiVersion: monitoring.coreos.com/v1
  kind: ServiceMonitor
  metadata:
    annotations:
      meta.helm.sh/release-name: monitoring
      meta.helm.sh/release-namespace: ai-obs
    creationTimestamp: "2026-01-06T05:55:13Z"
    generation: 1
    labels:
      app: kube-prometheus-stack-prometheus
      app.kubernetes.io/instance: monitoring
      app.kubernetes.io/managed-by: Helm
      app.kubernetes.io/part-of: kube-prometheus-stack
      app.kubernetes.io/version: 80.11.0
      chart: kube-prometheus-stack-80.11.0
      heritage: Helm
      release: monitoring
    name: monitoring-kube-prometheus-prometheus
    namespace: ai-obs
    resourceVersion: "143570"
    uid: 37685e6c-16d5-472a-b2a9-828cbc628512
  spec:
    endpoints:
    - path: /metrics
      port: http-web
    - path: /metrics
      port: reloader-web
    namespaceSelector:
      matchNames:
      - ai-obs
    selector:
      matchLabels:
        app: kube-prometheus-stack-prometheus
        release: monitoring
        self-monitor: "true"
- apiVersion: monitoring.coreos.com/v1
  kind: ServiceMonitor
  metadata:
    annotations:
      meta.helm.sh/release-name: monitoring
      meta.helm.sh/release-namespace: ai-obs
    creationTimestamp: "2026-01-06T05:55:13Z"
    generation: 1
    labels:
      app.kubernetes.io/component: metrics
      app.kubernetes.io/instance: monitoring
      app.kubernetes.io/managed-by: Helm
      app.kubernetes.io/name: kube-state-metrics
      app.kubernetes.io/part-of: kube-state-metrics
      app.kubernetes.io/version: 2.17.0
      helm.sh/chart: kube-state-metrics-7.0.0
      release: monitoring
    name: monitoring-kube-state-metrics
    namespace: ai-obs
    resourceVersion: "143572"
    uid: 82ea0017-46cc-4a24-ab17-8db49742769a
  spec:
    endpoints:
    - honorLabels: true
      port: http
    jobLabel: app.kubernetes.io/name
    selector:
      matchLabels:
        app.kubernetes.io/instance: monitoring
        app.kubernetes.io/name: kube-state-metrics
- apiVersion: monitoring.coreos.com/v1
  kind: ServiceMonitor
  metadata:
    annotations:
      meta.helm.sh/release-name: monitoring
      meta.helm.sh/release-namespace: ai-obs
    creationTimestamp: "2026-01-06T05:55:13Z"
    generation: 1
    labels:
      app.kubernetes.io/component: metrics
      app.kubernetes.io/instance: monitoring
      app.kubernetes.io/managed-by: Helm
      app.kubernetes.io/name: prometheus-node-exporter
      app.kubernetes.io/part-of: prometheus-node-exporter
      app.kubernetes.io/version: 1.10.2
      helm.sh/chart: prometheus-node-exporter-4.49.2
      release: monitoring
    name: monitoring-prometheus-node-exporter
    namespace: ai-obs
    resourceVersion: "143574"
    uid: f18cb243-5e2c-4315-a019-13beb874def2
  spec:
    attachMetadata:
      node: false
    endpoints:
    - port: http-metrics
      scheme: http
    jobLabel: jobLabel
    selector:
      matchLabels:
        app.kubernetes.io/instance: monitoring
        app.kubernetes.io/name: prometheus-node-exporter
kind: List
metadata:
  resourceVersion: ""