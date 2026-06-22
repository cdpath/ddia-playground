---
title: "Garbage Collection (SSD)"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [storage, ssd, hardware]
---

# Garbage Collection (SSD)

**Garbage collection**（GC）在 SSD 上下文中指闪存控制器为回收可擦除块而执行的内部操作。由于闪存只能按 page（通常 4 KiB）读写、按 block（通常 512 KiB）擦除，SSD 必须先把 block 中仍有效的 page 复制到别处，才能擦除整个 block。

## 说明

- **顺序写**：一个 block 中的 page 通常属于同一个文件。文件删除后，整个 block 可以直接擦除，无需 GC。
- **随机写**：一个 block 中的 page 来自多个文件，部分 page 已失效。擦除前必须先复制有效 page，产生额外写放大和延迟。

因此，即使 SSD 没有机械磁头，顺序写仍然比随机写更高效。

## 影响

- GC 消耗本可用于应用写入的带宽。
- 增加 SSD 磨损（闪存擦写次数有限）。
- 随机写会加剧 GC 负担。

## 相关

- [[sequential-write]]
- [[random-write]]
- [[write-amplification]]
- [[storage-engine]]
- [[chapter-04]]
